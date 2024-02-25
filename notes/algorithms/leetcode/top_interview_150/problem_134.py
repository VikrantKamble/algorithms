def can_complete_circuit(gas, cost) -> bool:

    can_complete = False

    for starting_pos in range(len(gas)):

        gas_in_tank = 0

        k = 0
        while k < len(gas):
            i = (k + starting_pos) % len(gas)

            # Fill in the gas
            gas_in_tank += gas[i]

            # Can we reach the next station
            if gas_in_tank < cost[i]:
                break
            else:
                # Once we reached, how much gas is left
                gas_in_tank -= cost[i]
            k += 1

        if k == len(gas):
            can_complete = True

    return can_complete


def can_complete_circuit_simplified(gas, cost):
    if sum(gas) < sum(cost):
        return -1

    # If the above condition is true, then it implies that there is
    # a solution
    total, res = 0, 0
    for i in range(len(gas)):
        total += gas[i] - cost[i]

        if total < 0:
            total = 0
            res = i + 1

    return res


if __name__ == "__main__":
    print(can_complete_circuit_simplified(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))

    # print(can_complete_circuit(gas=[2, 3, 4], cost=[3, 4, 3]))
