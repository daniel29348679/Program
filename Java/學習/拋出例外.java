import java.util.Scanner;
import java.lang.*;


public class 拋出例外
{
    public static void main(String[] args)
    {
        int k = 0;


        while (true)
        {
            try{
                Scanner scanner = new Scanner(System.in);
                int     a, b;

                a = scanner.nextInt();
                b = scanner.nextInt();

                if (b == 0)
                    throw new 零例外("NONONO!");
                k += a / b;
            }
            catch (零例外 e) {
                System.out.println("錯誤(分母不能為零)" + e.getMessage());
            }
            finally{
                System.out.println("現在=" + k);
            }
        }
    }
}
class 零例外 extends Exception{
    public 零例外(String str)
    {
        super(str);
    }
}