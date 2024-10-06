using System;
using System.Numerics;

public class RSA
{
    private BigInteger p, q, n, phi, e, d;

    public RSA()
    {
        GenerateKeys();
    }

    private void GenerateKeys()
    {
        p = 61; 
        q = 53;
        n = p * q;
        phi = (p - 1) * (q - 1);
        e = 17; //Einfache Wahl für e
        d = ModInverse(e, phi);
    }

    private BigInteger ModInverse(BigInteger a, BigInteger m)
    {
        BigInteger m0 = m, x0 = 0, x1 = 1;
        if (m == 1) return 0;
        while (a > 1)
        {
            BigInteger q = a / m;
            BigInteger t = m;
            m = a % m;
            a = t;
            t = x0;
            x0 = x1 - q * x0;
            x1 = t;
        }
        if (x1 < 0) x1 += m0;
        return x1;
    }

    public BigInteger Encrypt(BigInteger plaintext)
    {
        return BigInteger.ModPow(plaintext, e, n);
    }

    public BigInteger Decrypt(BigInteger ciphertext)
    {
        return BigInteger.ModPow(ciphertext, d, n);
    }
}

//Beispiel der Benutzung
class Program
{
    static void Main()
    {
        RSA rsa = new RSA();
        BigInteger message = 42; 
        BigInteger encrypted = rsa.Encrypt(message);
        Console.WriteLine("Verschlüsselt: " + encrypted);
        BigInteger decrypted = rsa.Decrypt(encrypted);
        Console.WriteLine("Entschlüsselt: " + decrypted);
    }
}
