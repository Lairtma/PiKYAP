
class Lab1
{
    static float get_arg(string co)
    {
        Console.WriteLine("Введите коэффициент " + co);
        string coof_str = Console.ReadLine();
        while (true)
        {
            try
            {
                return float.Parse(coof_str);
            }
            catch (Exception)
            {
                Console.WriteLine("Ошибка ввода, повторите: ");
                coof_str = Console.ReadLine();
            }
        }
    }

    static void get_roots(float a, float b, float c)
    {
        if (a == 0)
            Console.WriteLine("Не биквадратное уравнение");
        else
        {
            double d = b * b - (4 * a * c);
            if (d > 0)
            {
                d = Math.Sqrt(d);
                for (int i = -1; i <= 1; i += 2)
                {
                    double pre_ans = (d * i - b) / (2 * a);
                    if (pre_ans > 0)
                        Console.WriteLine("Корни " + Math.Sqrt(pre_ans).ToString() + " -" + Math.Sqrt(pre_ans).ToString());
                    else if (pre_ans == 0)
                        Console.WriteLine("Корень 0");
                }
            }
            else if (d == 0)
                Console.WriteLine("Корень 0");
            else
                Console.WriteLine("Нет корней");
        }
    }
    static void Main(string[] args)
    {
        float a, b, c;
        if (args.Length == 0)
        {
            a = get_arg("A");
            b = get_arg("B");
            c = get_arg("C");
        }
        else
        {
            a = float.Parse(args[0]);
            b = float.Parse(args[1]);
            c = float.Parse(args[2]);
        }
        get_roots(a, b, c);
    }
}
