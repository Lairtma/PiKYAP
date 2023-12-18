
class Lab2
{
    static int m(char a, char b)
    {
        if (a == b)
            return 0;
        return 1;
    }
    static void get_leven(string a, string b)
    {
        int[,] mas = new int[a.Length + 1, b.Length + 1];
        for (int i = 0; i <= a.Length; i++)
            for (int j = 0; j <= b.Length; j++)
            {
                if (Math.Min(i, j) == 0)
                    mas[i, j] = Math.Max(i, j);
                else
                    mas[i, j] = Math.Min(mas[i - 1, j] + 1, Math.Min(mas[i, j - 1] + 1, mas[i - 1, j - 1] + m(a[i - 1], b[j - 1])));
            }
        Console.WriteLine(mas[a.Length, b.Length]);
    }
    static void get_dameru_leven(string a, string b)
    {

    }

    static void Main(string[] args)
    {
        string a, b;
        Console.Write("Введите первое слово: ");
        a = Console.ReadLine();
        Console.Write("Введите второе слово: ");
        b = Console.ReadLine();
        Console.Write("Расстояние Левенштейна: ");
        get_leven(a, b);
    }
}
