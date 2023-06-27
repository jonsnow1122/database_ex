package src;

import java.sql.*;
import java.util.*;
import java.io.*;

public class C896PRO {

	// 以下代码将获取数据库连接操作封装为一个接口，可通过给定用户名和密码来连接数据库。
	public static Connection getConnect(String username, String passwd) {
		// 驱动类。
		String driver = "org.postgresql.Driver";
		// 数据库连接描述符。
		String sourceURL = "jdbc:postgresql://192.168.56.102:26000/mydb";
		Connection conn = null;

		try {
			// 加载驱动。
			Class.forName(driver);
		} catch (Exception e) {
			e.printStackTrace();
			return null;
		}

		try {
			// 创建连接。
			conn = DriverManager.getConnection(sourceURL, username, passwd);
			System.out.println("Connection succeed!");
		} catch (Exception e) {
			e.printStackTrace();
			return null;
		}

		return conn;
	};

	public static void main(String[] args) {
		// TODO 自动生成的方法存根
		new C896PRO();
		Connection conn = C896PRO.getConnect("zzy", "!1qaz2wsx");
		String fileName = "C:\\Users\\lenovo\\Desktop\\数据库实验\\data22.txt";

		try (Scanner sc = new Scanner(new FileReader(fileName))) {
			Statement statement = conn.createStatement();
			sc.nextLine(); // 跳过表头
			// sc.nextLine();
			// String sql = "insert into C896(cno,cname,period,credit,teacher)
			// values(?,?,?,?,?) ON DUPLICATE KEY UPDATE cName = cName";
			String sql = "insert into C896PRO(cno,cname,period,credit,teacher) values(?,?,?,?,?) ON DUPLICATE KEY UPDATE cName = CNAME";
			PreparedStatement ps = null;

			try {
				ps = conn.prepareStatement(sql);

				for (int i = 0; i < 1001; i++) {
					String line = sc.nextLine();
					String[] tmp = line.split("	");
					ps.setObject(1, tmp[0]); // Cno
					ps.setObject(2, tmp[1]); // Cname
					ps.setObject(3, tmp[2]); // period
					ps.setObject(4, tmp[3]); // credit
					ps.setObject(5, tmp[4]); // teacher

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

	public static double NormalDistribution(float u, float v) {
		java.util.Random random = new java.util.Random();
		return Math.sqrt(v) * random.nextGaussian() + u;
	}
}