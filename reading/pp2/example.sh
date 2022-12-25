#!/bin/bash
A=123
(A=abc;echo $A);echo $A
{ A=abc;echo $A; };echo $A
