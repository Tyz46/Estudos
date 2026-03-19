/*
public class Exemplo1 {
	public Exemplo1(){
	}
	public void mostrarMensagem(String msg){
		System.out.println(msg);
	}
	public static void main(String[] args){
		Exemplo1 ex1 = new Exemplo1();
		ex1.mostrarMensagem("Teste com Exemplo1");
	}
}
*/

/*
public class Exemplo1 {
	public Exemplo1(){
	}
	public void mostrarMensagem(String msg){
		System.out.println(msg);
	}
	public static void main(String[] args){
		Exemplo1 ex1;
		Exemplo1 meuPet;
		System.out.println("Antes de inscia");
		ex1 = new Exemplo1();
		ex1.mostrarMensagem("Teste");
		meuPet = new Exemplo1();
		meuPet.mostrarMensagem("esta é a mensagem do meu pet lindo");
	}
}
*/
/*
public class Exemplo1 {
	String msg;
	public Exemplo1(String m){
		msg = m;
	}
	public void mostrarMensagem(){
		System.out.println(msg);
	}
	public static void main(String[] args){
		Exemplo1 ex1 = new Exemplo1("Este é o texto da mensagem");
		ex1.mostrarMensagem();
		Exemplo1 ex31 = new Exemplo1("Um texto qualquer");
		ex31.mostrarMensagem();
	}
}
*/
/*
public class Exemplo1 {
	String msg;
	public Exemplo1(){
		msg = "";
	}
	public static void main(String[] args){
		Exemplo1 e1 = new Exemplo1();
		e1.msg="este é um texto";
		Exemplo1 e2;
		e2=e1;
		System.out.println("Comparando os objetos");
		System.out.println(e1.equals(e2));

	}
}
*/
/*
public class Exemplo1 {
	public static void main(String[] args){
		String s1 = "este é um texto";
		String s2 = "este é um texto";
		System.out.println("Exemplo1 ");
		System.out.println("Comparando Strings ");
		System.out.println(s1==s2);
		System.out.println("Comparando os objetos agora utilizando equals: ");
		System.out.println(s1.equals(s2));
	}
}
*/

public class Exemplo1 {
	String msg;
	public Exemplo1(){
		msg = "";
	}
	public void mostrarMsg(){
		System.out.println(msg);
	}
	public static void main(String[] args){
		System.out.println("Argumento 1: " + args[0]);
		Exemplo1 ex = new Exemplo1();
		ex.msg = args[0];
		ex.mostrarMsg();
	}
}