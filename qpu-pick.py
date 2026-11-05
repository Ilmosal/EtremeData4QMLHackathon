"""Pick a Resonance machine for a job from the live queue state.

As a library:   alias = qpu_pick.pick_machine(qubits=5)
As a launcher:  python qpu_pick.py --qubits 5 -- python my_job.py

The launcher sets IQM_SERVER_URL and IQM_QUANTUM_COMPUTER, which the IQM
client reads when the script does not name a machine itself.
"""

import argparse
import os
import random
import sys
from datetime import datetime, timedelta, timezone

import requests

SERVER = "https://resonance.iqm.tech"
API = SERVER + "/api/v1"


def get(path, token):
    response = requests.get(API + path, headers={"Authorization": "Bearer " + token}, timeout=10)
    response.raise_for_status()
    return response.json()


def runs_now(windows, now):
    # The server stamps the current window's start with its own clock, which
    # can run ahead of ours. Allow a minute of skew.
    soon = now + timedelta(minutes=1)
    return any(
        datetime.fromisoformat(w["start"]) <= soon and now < datetime.fromisoformat(w["end"])
        for w in windows
    )


def machine_states(token):
    now = datetime.now(timezone.utc)
    states = []
    for machine in get("/quantum-computers", token)["quantum_computers"]:
        alias = machine["alias"]
        detail = get("/quantum-computers/" + alias, token)
        queue = get("/quantum-computers/%s/queue-availability" % alias, token)
        mock = detail["backend_type"] == "mock"
        # Free mocks list no run windows at all, yet they run jobs at any time.
        in_window = mock or runs_now(queue["available"], now)
        states.append({
            "alias": alias,
            "mock": mock,
            "qubits": detail["number_of_qubits"],
            "price": float(detail["pricing"]["payg_price_per_second"]),
            "queue": queue["queue_length"],
            "ready": detail["operational_status"] == "online"
            and detail["health"]["healthy"]
            and in_window,
        })
    return states


def pick_machine(qubits, token=None, mock=False, slack=1):
    """Return a ready machine with enough qubits and a short queue.

    Picks at random among machines within `slack` jobs of the shortest queue,
    so that many users who ask at the same moment do not all pick one machine.
    Mock mode only picks free mocks: the API prices some mocks above zero.
    """
    token = token or os.environ["IQM_TOKEN"]
    fits = [
        s for s in machine_states(token)
        if s["ready"] and s["mock"] == mock and s["qubits"] >= qubits
        and not (mock and s["price"] > 0)
    ]
    if not fits:
        raise RuntimeError(
            "no %s machine with %d or more qubits takes jobs now"
            % ("free mock" if mock else "real", qubits)
        )
    shortest = min(s["queue"] for s in fits)
    return random.choice([s for s in fits if s["queue"] <= shortest + slack])["alias"]


def main():
    parser = argparse.ArgumentParser(description="Run a command on the least busy machine.")
    parser.add_argument("--qubits", type=int, required=True)
    parser.add_argument("--mock", action="store_true", help="pick a free mock machine")
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("give the command to run after --")
    alias = pick_machine(args.qubits, mock=args.mock)
    print("qpu_pick: running on %s" % alias, file=sys.stderr)
    os.environ["IQM_SERVER_URL"] = SERVER
    os.environ["IQM_QUANTUM_COMPUTER"] = alias
    os.execvp(command[0], command)


if __name__ == "__main__":
    main()
