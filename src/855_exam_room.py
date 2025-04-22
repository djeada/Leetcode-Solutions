import bisect

class ExamRoom:
    def __init__(self, total_seats: int):
        self.total_seats = total_seats
        self.occupied = []  # sorted list of occupied seat indices

    def seat(self) -> int:
        occupied = self.occupied
        total_seats = self.total_seats

        if not occupied:
            occupied.append(0)
            return 0

        # 1) consider the leftmost seat
        chosen_seat = 0
        max_distance = occupied[0]

        # 2) scan gaps between occupied seats
        previous_seat = occupied[0]
        for next_seat in occupied[1:]:
            distance = (next_seat - previous_seat) >> 1  # floor((next - prev)/2)
            if distance > max_distance:
                max_distance = distance
                chosen_seat = previous_seat + distance
            previous_seat = next_seat

        # 3) consider the rightmost seat
        end_distance = (total_seats - 1) - occupied[-1]
        if end_distance > max_distance:
            chosen_seat = total_seats - 1

        # insert chosen seat in sorted order
        bisect.insort(occupied, chosen_seat)
        return chosen_seat

    def leave(self, p: int) -> None:
        # remove p from the occupied list
        index = bisect.bisect_left(self.occupied, p)
        self.occupied.pop(index)
