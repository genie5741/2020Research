#!/bin/bash

echo do 30
cd 30
./runCaseKEpsilon
cd ..
echo done 30

echo do 45
cd 45
./runCaseKEpsilon
cd ..
echo done 45

echo do 60
cd 60
./runCaseKEpsilon
cd ..
echo done 60

echo do 90
cd base
./runCaseKEpsilon
cd ..
echo done 90

echo do ConcaveBigCycloid
cd ConcaveBigCycloid
./runCaseKEpsilon
cd ..
echo done ConcaveBigCycloid

echo do ConcaveQuadrant
cd ConcaveQuadrant
./runCaseKEpsilon
cd ..
echo done ConcaveQuadrant

echo do ConcaveSmallCycloid
cd ConcaveSmallCycloid
./runCaseKEpsilon
cd ..
echo done ConcaveSmallCycloid

echo do ConvexBigCycloid
cd ConvexBigCycloid
./runCaseKEpsilon
cd ..
echo done ConvexBigCycloid

echo do ConvexQuadrant
cd ConvexQuadrant
./runCaseKEpsilon
cd ..
echo done ConvexQuadrant

echo do ConvexSmallCycloid
cd ConvexSmallCycloid
./runCaseKEpsilon
cd ..
echo done ConvexSmallCycloid

echo all done
