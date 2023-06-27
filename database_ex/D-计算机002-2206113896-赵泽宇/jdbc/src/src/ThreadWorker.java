import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.Statement;
import java.io.File;
import java.io.BufferedReader;
import java.io.FileReader;

class Insert implements Runnable {
    private Thread t;
    private String threadName;

    Insert(String name) {
        threadName = name;
    }

    public void run() {
        try {
        Class.forName("org.postgresql.Driver");
        String url = "jdbc:postgresql://192.168.56.102:26000/mydb";
        try {
            // 加载驱动。
            Class.forName(driver);
        } catch (Exception e) {
        e.printStackTrace();
        }

        try {
            // 创建连接。
            conn = DriverManager.getConnection(sourceURL, username, passwd);
            System.out.println("Connection succeed!");
        } catch (Exception e) {
        e.printStackTrace();
        }
        BufferedReader readerStream = new BufferedReader(new FileReader(fp));
        String lineData = "";
		try (Scanner sc = new Scanner(new FileReader(fileName))) {
			Statement statement = conn.createStatement();
			sc.nextLine(); // 跳过表头
			// sc.nextLine();
			// String sql = "insert into C896(cno,cname,period,credit,teacher)
			// values(?,?,?,?,?) ON DUPLICATE KEY UPDATE cName = cName";
			String sql = "insert into SC896(sno,cno,grade) values(?,?,?) ON DUPLICATE KEY UPDATE grade = grade";
			PreparedStatement ps = null;

			try {
				ps = conn.prepareStatement(sql);

				for (int i = 0; i < 20000; i++) {
					String line = sc.nextLine();
					String[] tmp = line.split("	");
					// System.out.println(tmp[1]);
					String sno = tmp[0];
					ps.setObject(1, sno);

					String cno = tmp[1];
					ps.setObject(2, cno);

					ps.setObject(3, tmp[2]);

					ps.execute();
				}
			} catch (SQLException e) {
				e.printStackTrace();
			} finally {
				statement.close();
			}
		} catch (Exception e) {

		}
		try {
			conn.close();
		} catch (Exception e) {

		}
}

   

    public void start () {
        if (t == null) {
           t = new Thread (this, threadName);
           t.start ();
        }
    }
}

class Delete implements Runnable {
      
    private Thread t;
    private String threadName;

      

    Delete(String name) {
        threadName = name;
}

      

    public void run() {
    try {
        Class.forName("org.postgresql.Driver");
        String url = "jdbc:postgresql://192.168.56.102:26000/mydb";
        try {
            // 加载驱动。
            Class.forName(driver);
        } catch (Exception e) {
        e.printStackTrace();
        }

        try {
            // 创建连接。
            conn = DriverManager.getConnection(sourceURL, username, passwd);
            System.out.println("Connection succeed!");
        } catch (Exception e) {
        e.printStackTrace();
        }
        BufferedReader readerStream = new BufferedReader(new FileReader(fp));
        String lineData = "";
		try (Scanner sc = new Scanner(new FileReader(fileName))) {
			Statement statement = conn.createStatement();
			sc.nextLine(); // 跳过表头
			// sc.nextLine();
			// String sql = "insert into C896(cno,cname,period,credit,teacher)
			// values(?,?,?,?,?) ON DUPLICATE KEY UPDATE cName = cName";
			String sql = "delete where grade<60";
			PreparedStatement ps = null;

			try {
				ps = conn.prepareStatement(sql);

				for (int i = 0; i < 200; i++) {
					String line = sc.nextLine();
					String[] tmp = line.split("	");
					// System.out.println(tmp[1]);
					String sno = tmp[0];
					ps.setObject(1, sno);

					String cno = tmp[1];
					ps.setObject(2, cno);

					ps.setObject(3, tmp[2]);

					ps.execute();
				}
			} catch (SQLException e) {
				e.printStackTrace();
			} finally {
				statement.close();
			}
		} catch (Exception e) {

		}
		try {
			conn.close();
		} catch (Exception e) {

		}
}

   

    public void start () {
        if (t == null) {
           t = new Thread (this, threadName);
           t.start ();
        }
    }
}
