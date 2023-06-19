import java.util.Scanner;

class Animal {
    public int k = 0;
}
class Dog extends Animal {}
class Cat extends Animal {}
public class test {
    public static void main(String[] args)
    {
        Animal a0 = new Animal();
        Animal a1 = new Dog();
        Animal a2 = new Cat();
        Dog    a3 = new Dog();
        Cat    a4 = new Cat();

        a0 = a1;
        //a3 = a4;
        //a4 = a2;
        //a2 = (Cat)a1;
        a3 = (Dog)a0;
        a4 = (Cat)a2;
        System.out.println("haha");

        Dog    d = new Dog();
        Animal a = d;

        a.k = 900;
        System.out.println("!" + a.k + "," + d.k);
    }
}
