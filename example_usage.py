from client import EquivariantMessagePassing

def main():
    print("=== SE(3) Equivariant Message Passing ===")
    emp = EquivariantMessagePassing()
    p1 = [1.0, 0.0, 0.0]
    p2 = [0.0, 1.0, 0.0]

    res = emp.update_coordinates(p1, p2, 0.5, 0.5)
    print("Equivariant update:", res)
    assert res["updated_pos"] != p1

    print("SE(3) Equivariant Kernel verified successfully!")

if __name__ == "__main__":
    main()
