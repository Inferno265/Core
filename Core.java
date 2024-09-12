package javax.game;

import java.io.File;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
public class Core {
	
	private static int gameinfo;
	private static int program;
	public static boolean game = false;

	public static boolean init() {
		File gameinfo = new File("gameinfo.gi");
		if (gameinfo.exists()) {
			game = true;
			return true;
		} else {
			JFrame f = new JFrame("");
			JOptionPane.showMessageDialog(f, "gameinfo.gi does not exist in the current location.", "Engine Error", JOptionPane.ERROR_MESSAGE);
			game = false;
			return false;
		}
	}
	
	public static void loadgiRAM(int x) {
		gameinfo = x;
		return;
	}

}
