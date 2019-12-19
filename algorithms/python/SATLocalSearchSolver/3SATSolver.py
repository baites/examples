#! /usr/bin/env python

import math
import sys

def parse_input():
    """Parse input."""
    n, m = map(int, input().split())
    clauses = [ list(map(int, input().split())) for i in range(m) ]
    return n, clauses


def branch_candidate(candidate, clauses):
    """Check a candidate solution agains clauses."""
    # Loop over all the clauses
    for clause in clauses:
        # Loop over all the literals
        satisfy = False
        # Loop over literals and check for satifibility
        for literal in clause:
            # Get literal index and value
            lindex = abs(literal) - 1
            lvalue = (candidate >> lindex) & 1
            # Check id literal is satisfied
            satisfy |= lvalue == (literal > 0)
        # If no satisfy generate branching candidates
        if not satisfy:
            # Flip bits to branch out candidate
            candidates = []
            for literal in clause:
                lindex = abs(literal) - 1
                candidates.append(candidate ^ (1 << lindex))
            return candidates
    return []


def local_solver(n, clauses):

    # Initialize the stack
    stack = [
        (2**n-1, int(math.ceil(n/2))),
        (0, int(math.ceil(n/2)))
    ]

    # Iterate and branchout candidate
    while len(stack) > 0:
        # Pop and candidate and radius from stack
        candidate, radius = stack.pop()
        # Branchout candidate if does not safisfy clauses
        candidates = branch_candidate(
            candidate, clauses
        )
        # If no branches then candidate satisfy clauses
        if len(candidates) == 0:
            return candidate
        # Check if radius is not zero
        if radius == 0:
            continue
        # Add branchout candidates to the stack
        for candidate in reversed(candidates):
            stack.append((candidate, radius - 1))

    return None


def parse_cnf_format(filename):
    """Read and cnf file."""
    clauses = []
    with open(filename) as handler:
        for line in handler.readlines():
            if line.startswith('c'):
                continue
            if line.startswith('p cnf'):
                n = int(line.split()[2])
                continue
            clauses.append(
                [int(literal) for literal in line.split()[:-1]]
            )
    return n, clauses


n, clauses = parse_cnf_format(sys.argv[1])
solution = local_solver(n, clauses)

if solution is None:
    print('UNSATISFIABLE')
else:
    print('SATISFIABLE')
    output = ''
    for index in range(1,n+1):
        if solution & 1:
            output += ' {}'.format(index)
        else:
            output += ' -{}'.format(index)
        solution = solution >> 1
    print(output)
