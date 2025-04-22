from typing import Dict, List, Tuple, Optional

class Solution:
    def __init__(self) -> None:
        self._key_positions = self._build_keyboard_layout()
        self._keys = sorted(self._key_positions.keys())
        self._off_key_index = len(self._keys)
        self._key_to_index = self._create_key_index_map()
        self._distance_matrix = self._build_distance_matrix()

    @staticmethod
    def _build_keyboard_layout() -> Dict[str, Tuple[int, int]]:
        rows = [
            ["A", "B", "C", "D", "E", "F"],
            ["G", "H", "I", "J", "K", "L"],
            ["M", "N", "O", "P", "Q", "R"],
            ["S", "T", "U", "V", "W", "X"],
            ["Y", "Z"],
        ]
        return {
            key: (row_idx, col_idx)
            for row_idx, row in enumerate(rows)
            for col_idx, key in enumerate(row)
        }

    def _create_key_index_map(self) -> Dict[Optional[str], int]:
        index_map: Dict[Optional[str], int] = {}
        for idx, key in enumerate(self._keys):
            index_map[key] = idx
        index_map[None] = self._off_key_index
        return index_map

    def _build_distance_matrix(self) -> List[List[int]]:
        count = len(self._keys)
        matrix: List[List[int]] = [[0] * count for _ in range(count)]

        for i, key1 in enumerate(self._keys):
            for j, key2 in enumerate(self._keys):
                pos1 = self._key_positions[key1]
                pos2 = self._key_positions[key2]
                matrix[i][j] = abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])

        return matrix

    def _move_cost(self, from_idx: int, to_idx: int) -> int:
        if from_idx == self._off_key_index:
            return 0
        return self._distance_matrix[from_idx][to_idx]

    def minimumDistance(self, word: str) -> int:
        """
        Uses an iterative DP over the reversed word to fill a 2D table:
        dp_table[f1][f2] = minimum cost to type the remaining suffix
        when finger1 is on key f1 and finger2 is on key f2.
        """
        num_keys = len(self._keys)
        off = self._off_key_index

        # Initialize DP table with zeros for the empty suffix
        dp_table: List[List[int]] = [[0] * (num_keys + 1) for _ in range(num_keys + 1)]

        # Process each character in reverse order
        for char in reversed(word):
            target = self._key_to_index[char]

            # Snapshot the old values before overwriting
            previous_target_row = dp_table[target][:]
            previous_target_col = [dp_table[r][target] for r in range(num_keys + 1)]

            for finger1_pos in range(num_keys + 1):
                for finger2_pos in range(num_keys + 1):
                    cost_if_f1_moves = (
                        previous_target_row[finger2_pos]
                        + self._move_cost(finger1_pos, target)
                    )
                    cost_if_f2_moves = (
                        previous_target_col[finger1_pos]
                        + self._move_cost(finger2_pos, target)
                    )
                    dp_table[finger1_pos][finger2_pos] = min(
                        cost_if_f1_moves,
                        cost_if_f2_moves
                    )

        # Both fingers start off-key
        return dp_table[off][off]
        
