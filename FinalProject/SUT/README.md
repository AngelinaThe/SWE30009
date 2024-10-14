# SWE30009 Final Project Task 2

## 1. Introduction

In this task, the student is required to test a real-world program of their choice using metamorphic testing and evaluate their testing using mutation testing. The student is required to propose and describe at least two metamorphic relations (and at least five metamorphic test groups for each metamorphic relation). The selected program is neither too large and complex nor too simple so that you can generate at least 30 nonequivalent mutants from the original program.

## 2. Chosen Program: Merge Sort Algorithm

I have chosen to do the merge sort algorithm for Task 2. The merge sort algorithm is a divide-and-conquer sorting technique. It works by recursively dividing the array into two halves, sorting each half, and then merging the sorted halves. Below is the implementation of the merge sort algorithm used in this assignment.

The Merge Sort Algorithm used is from https://github.com/B3ns44d/Python_Sorting_Algorithms/blob/master/Merge_Sort.py

## 3. Where to find everything?
SUT > program.py        --->  Original Merge Sort Program from Github.
SUT > input_data.txt    --->  Sample data for merge sort program.

MUTANTS > program_mutant.py        --->  Mutation Testing Script.
MUTANTS > mutant_test_cases.py     --->  Mutation Test Cases used in Testing Script. There are 10 test cases.
MUTANTS > mutant_functions.py      --->  Mutatant Functions used in Testing Script. There are 20 mutant functions.
Note: 20 x 10 = 200, generates > 30 required non-equivalent mutants.

TEST > program_metamorphic.py       ---> Metamorphic Testing Script.
TEST > metamorphic_test_cases.txt   ---> Test Cases used in Metamorphic Testing. Each MR has its own test cases.
TEST > metamorphic_relation.txt     ---> Metamorphic Relations used in Metamorphic Testing. Total of 3 MRs.