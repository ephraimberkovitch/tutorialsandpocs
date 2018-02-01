#include <stdlib.h>
#include <stdio.h>
#include <cs50.h>

void swap(int *a,int *b)
{
    int t = *a;
    *a = *b;
    *b = t;
}

/* Arrange the N elements of ARRAY in random order.
   Only effective if N is much smaller than RAND_MAX;
   if this may not be the case, use a better random
   number generator. */
void shuffle(int *array, size_t n)
{
    if (n > 1) 
    {
        size_t i;
        for (i = 0; i < n - 1; i++) 
        {
          size_t j = i + rand() / (RAND_MAX / (n - i) + 1);
          int t = array[j];
          array[j] = array[i];
          array[i] = t;
        }
    }
}

int linear_search(int *array, size_t n, int target)
{
    int res = -1;
    int i = 0;
    while (i<n)
    {
        if (array[i]==target)
        {
            res = i;
            break;
        }
        i++;
    }
    return res;
}

int binary_search(int *array, size_t n, int target)
{
    int found = 0;
    insertion_sort(array,n);
    int index = n/2;
    while(!found)
    {
        if (array[index]==target)
        {
            found = true;
            break;
        }
        n /= 2;
        if (n<1)
        {
            found = false;
            break;
        }
        else if (target<array[index])
        {
            index -= n;
        }
        else //target>array[index]
        {
            index += n;
        }
    }
    return found;
}

void merge(int *a, int low, int high, int mid, size_t n)
{
    int i, j, k, c[n];
    i = low;
    k = low;
    j = mid + 1;
    while (i <= mid && j <= high)
    {
        if (a[i] < a[j])
        {
            c[k] = a[i];
            k++;
            i++;
        }
        else
        {
            c[k] = a[j];
            k++;
            j++;
        }
    }
    while (i <= mid)
    {
        c[k] = a[i];
        k++;
        i++;
    }
    while (j <= high)
    {
        c[k] = a[j];
        k++;
        j++;
    }
    for (i = low; i < k; i++)
    {
        a[i] = c[i];
    }
}

void mergesort(int *a, int low, int high, size_t n)
{
    int mid;
    if (low < high)
    {
        mid=(low+high)/2;
        mergesort(a,low,mid,n);
        mergesort(a,mid+1,high,n);
        merge(a,low,high,mid,n);
    }
    return;
}

void merge_sort(int *array, size_t n)
{
    mergesort(array, 0, n-1, n);
}

void bubble_sort(int *array, size_t n)
{
	int swaps = -1;
	do
	{
		swaps = 0;
		for(int i=0; i<n-1; i++)
		{
			if(array[i]>array[i+1])
			{
			    swap(&array[i],&array[i+1]);
			    swaps++;
			}
		}
	}
	while (swaps>0);
}

void another_bubble_sort(int *array, size_t n)
{
	for(int x=0; x<n-1; x++)
	{
		for(int y=x; y<n; y++)
		{
			if(array[x]>array[y])
			{
			    swap(&array[x],&array[y]);
			}
		}
	}
}

void selection_sort(int *array, size_t n)
{
	for(int x=0; x<n; x++)
	{
		int index_of_min = x;
		for(int y=x; y<n; y++)
		{
			if(array[index_of_min]>array[y])
			{
				index_of_min = y;
			}
		}
		if (x!=index_of_min)
		{
		    swap(&array[x],&array[index_of_min]);
		}
	}
}

void insertion_sort(int *array, size_t n)
{
    for (int i=1;i<n;i++) //1st element is regarded to be sorted
    {
        int elem = array[i];
        eprintf("%d ",elem);
        int j = i-1;
        while (array[j]>elem&&j>=0)
        {
            array[j+1] = array[j];
            j--;
        }
        array[j+1] = elem;
    }
}


int main(int argc,string argv[])
{
    int x = 7, y = 9;
    swap(&x,&y);
    printf("Test swap: x=%d,y=%d",x,y);
    if (argc!=2)
    {
        printf("Syntax: sort_algorithms <length_of_array>");
        return 1;
    }
    int len = atoi(argv[1]);
    int arr[len];
    for(int i=0;i<len;i++)
        arr[i] = i+1;
    shuffle(arr,len);
    printf("\nArray: ");
    for(int i=0;i<len;i++)
        printf("%d ",arr[i]);
    //another_bubble_sort(arr,len);
    //bubble_sort(arr,len);
    //selection_sort(arr,len);
    //insertion_sort(arr,len);
    merge_sort(arr,len);
    printf("\nSorted Array: ");
    for(int i=0;i<len;i++)
        printf("%d ",arr[i]);
    printf("\n");
}