public class Main {
  public static void main(String[] args) {
    int a = --4;
    int r1 = a++;
    int r2 = ++a;
    System.out.println(r1+""+r2);
  }
}