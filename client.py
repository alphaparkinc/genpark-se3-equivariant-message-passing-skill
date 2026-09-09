import math

class EquivariantMessagePassing:
    """E(3) / SE(3) Equivariant Message Passing Kernel."""
    def update_coordinates(self, pos_i: list[float], pos_j: list[float],
                           scalar_feat_i: float, scalar_feat_j: float) -> dict:
        diff = [pos_i[k] - pos_j[k] for k in range(3)]
        dist_sq = sum(d ** 2 for d in diff)
        scale = math.exp(-dist_sq) * (scalar_feat_i + scalar_feat_j)
        new_pos_i = [round(pos_i[k] + diff[k] * scale, 5) for k in range(3)]

        return {
            "original_pos": pos_i,
            "updated_pos": new_pos_i,
            "squared_distance": round(dist_sq, 5),
            "equivariant_scale": round(scale, 5)
        }
