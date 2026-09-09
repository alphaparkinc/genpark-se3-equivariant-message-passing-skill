import sys
import json
from client import EquivariantMessagePassing

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "update_coords":
        emp = EquivariantMessagePassing()
        return emp.update_coordinates(params.get("p1", [0, 0, 0]), params.get("p2", [1, 1, 1]),
                                      params.get("f1", 1.0), params.get("f2", 1.0))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
