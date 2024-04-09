import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LoginSignupInterface extends JFrame implements ActionListener {
    // Components of the Form
    private Container c;
    private JLabel title;
    private JLabel username;
    private JTextField tusername;
    private JLabel password;
    private JPasswordField tpassword;
    private JButton loginBtn;
    private JButton signupBtn;

    // Constructor to setup GUI components and event handling
    public LoginSignupInterface() {
        setTitle("Login / Sign Up");
        setBounds(300, 90, 900, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setResizable(false);

        c = getContentPane();
        c.setLayout(null);

        title = new JLabel("Login / Sign Up");
        title.setFont(new Font("Arial", Font.PLAIN, 30));
        title.setSize(300, 30);
        title.setLocation(300, 30);
        c.add(title);

        username = new JLabel("Username");
        username.setFont(new Font("Arial", Font.PLAIN, 20));
        username.setSize(100, 20);
        username.setLocation(100, 100);
        c.add(username);

        tusername = new JTextField();
        tusername.setFont(new Font("Arial", Font.PLAIN, 15));
        tusername.setSize(190, 20);
        tusername.setLocation(200, 100);
        c.add(tusername);

        password = new JLabel("Password");
        password.setFont(new Font("Arial", Font.PLAIN, 20));
        password.setSize(100, 20);
        password.setLocation(100, 150);
        c.add(password);

        tpassword = new JPasswordField();
        tpassword.setFont(new Font("Arial", Font.PLAIN, 15));
        tpassword.setSize(190, 20);
        tpassword.setLocation(200, 150);
        c.add(tpassword);

        loginBtn = new JButton("Login");
        loginBtn.setFont(new Font("Arial", Font.PLAIN, 15));
        loginBtn.setSize(100, 20);
        loginBtn.setLocation(150, 200);
        loginBtn.addActionListener(this);
        c.add(loginBtn);

        signupBtn = new JButton("Sign Up");
        signupBtn.setFont(new Font("Arial", Font.PLAIN, 15));
        signupBtn.setSize(100, 20);
        signupBtn.setLocation(260, 200);
        signupBtn.addActionListener(this);
        c.add(signupBtn);

        setVisible(true);
    }

    // Method actionPerformed() to get the action performed
    // by the user and act accordingly
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == loginBtn) {
            JOptionPane.showMessageDialog(this, "Login Button Clicked");
        } else if (e.getSource() == signupBtn) {
            JOptionPane.showMessageDialog(this, "Sign Up Button Clicked");
        }
    }

    // Main method to run the program
    public static void main(String[] args) {
        new LoginSignupInterface();
    }
}
