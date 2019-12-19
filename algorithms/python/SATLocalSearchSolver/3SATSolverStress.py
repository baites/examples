#! /usr/bin/env python

import math
import random
import subprocess
import sys
import time


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
            # Set bits to negate the clause
            #for literal in clause:
            #    lindex = abs(literal) - 1
            #    lvalue = (candidate >> lindex) & 1
            #    # If literal and bit value 1 flip zero
            #    if literal > 0 and lvalue:
            #        candidate ^= (1 << lindex)
            #    # If not literal and bit value 0 flip 1
            #    elif literal < 0 and not lvalue:
            #        candidate ^= (1 << lindex)
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


def minisat_solver(n, clauses):
    """Write a N-SAT problem in cnf."""
    # Write input
    with open('tmp.cnf', 'w') as f:
        f.write('p cnf {} {}\n'.format(n, len(clauses)))
        for clause in clauses:
            f.write(' '.join([str(literal) for literal in clause]+['0'])+'\n')

    # Run program
    subprocess.run(['minisat', 'tmp.cnf', 'tmp.sat'], capture_output=True)

    # Parse ouput
    with open("tmp.sat", "r") as satfile:
        for line in satfile:
            if line.split()[0] == "UNSAT":
                return False
            elif line.split()[0] == "SAT":
                return True

if __name__ == '__main__':

    while 1:
        # Max number of literals
        k = 6
        # Number of variables
        n = random.randint(k, 40)
        # Number of clauses
        m = random.randint(1, 40)
        # Generate problem variables
        variables = []
        for variable in range(-n, n+1):
            if variable == 0:
                continue
            variables.append(variable)
        # Generate problem clauses
        clauses = []
        for i in range(m):
            nliterals = random.randint(1,k)
            clauses.append(random.sample(variables, nliterals))


        t0 = time.time()
        ref = minisat_solver(n, clauses)
        t1 = time.time()
        test = local_solver(n, clauses)
        t2 = time.time()

        if (test is not None) != ref:
            print('Error')
            sys.exit(1)
        else:
            print('OK %0.2fs' % (t2 - t1), 'x%0.2f' % ((t1 - t0)/(t2 - t1)))
