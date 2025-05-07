#include<iostream>
using namespace std;

void selection_sort(int arr[],int n)
{
    int i, j, min, temp;
    for(i=0; i<n-1; i++)
    {
        min=i;
        for(j=i+1; j<n; j++)
        {
            if(arr[j]<arr[min])
            {
                min=j;
            }
        }
        temp=arr[i];
        arr[i]=arr[min];
        arr[min]=temp;
    }
}
 
int main() {
    int n,arr[100];
    cout<<"ENTER THE NUMBER OF ELEMENTS: ";
    cin>>n;
    cout<<"ENTER THE "<<n<<" ELEMENTS:\n";
    for(int i=0; i<n; i++)
    {
        cin>>arr[i];
    }
    selection_sort(arr, n);
    cout<<"SORTED ARRAY: ";
    for (int i=0; i<n; i++)
    {
        cout<<arr[i]<<" ";
    }
    return 0;
}
