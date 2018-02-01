/**
 * helpers.c
 *
 * Helper functions for Problem Set 3.
 */
 
#include <cs50.h>

#include "helpers.h"

#define SIZE 65536

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
    if (n<=0)
        return false;
    sort(values,n);
    int from = 0, to = n-1;
    while (from<to && to-from>0)
    {
        int index = (to+from)/2;
        if (value==values[index])
            return true;
        if (value<values[index]) 
        {
            to = index;
        }
        else 
        {
            from = index;
        }
        if (from+1==to&&value!=values[from]&&value!=values[to])
            return false;
    }
    return false;
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    //bubble sort - general case
    for (int i=0;i<n-1;i++)
        for (int j=i+1;j<n;j++)
            if (values[i]>values[j]) 
            {
                int t = values[i];
                values[i] = values[j];
                values[j] = t;
            }
    //Special case - Assume that each of the array’s numbers will be non-negative and less than 65,536. But the array might contain duplicates.
    //The running time of your implementation must be in O(n)
    int array[SIZE];
    for (int i=0;i<SIZE;i++)
        array[i] = 0;
    for (int i=0;i<n;i++)
        array[values[i]-1]++;
    int index = 0;
    for (int i=0;i<SIZE;i++)
        if (array[i]>0)
            //for (int j=0;j<array[i];j++)
            {
                values[index] = i+1;
                index++;
            }
    return;
}
