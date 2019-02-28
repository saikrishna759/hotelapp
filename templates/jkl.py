import java.util.Scanner;
private class  sort{
  public static void main (String[] args) {
     Scanner sc = new Scanner(System.in);
     int t = sc.nextInt();
     int n = sc.nextInt();
     int array[] = new int[n];
     int s = sc.nextInt();
     while(t>0)
     {   int b=0;
         for(int i=0;i<n;i++)
         {
            array[i] = sc.nextInt(); 
         }
         for(int i=0;i<n;i++)
         {
             for(int j=i;j<n;j++)
             {
                b =+ array[j];
                if(b==s)
                {   
                    System.out.println(i);
                  System.out.println(j);
                    break;
                }
             }
         }
         
         t--;
                
     }
        
     
  }
}