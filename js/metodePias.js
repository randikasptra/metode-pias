let a, b, n;

document.getElementById("btn").onclick = function () {
  a = parseFloat(document.getElementById("a").value);
  b = parseFloat(document.getElementById("b").value);
  n = parseInt(document.getElementById("n").value);

  if (isNaN(a) || isNaN(b) || isNaN(n)) {
    alert(
      "HEIIII KAMU BELUM MASUKIN NILAII YAAA !!!\nbtw Frontend nya ganteng"
    );
    return;
  }

  const f = (x) => Math.exp(x); // Fungsi f(x) = e^x

  const hasilTrapesium = aturanTrapesium(f, a, b, n).toFixed(6);
  const hasilTitikTengah = titikTengah(f, a, b, n).toFixed(6);
  const hasilSegiempat = metodePiasKaidaSegiempat(f, a, b, n).toFixed(6);

  document.getElementById("trapesium").textContent = hasilTrapesium;
  document.getElementById("titikTengah").textContent = hasilTitikTengah;
  document.getElementById("segiEmpat").textContent = hasilSegiempat;
};

function aturanTrapesium(f, a, b, n) {
  let h = (b - a) / n;
  let x = Array.from({ length: n + 1 }, (_, i) => a + i * h);
  let y = x.map(f);
  let integral =
    (h / 2) *
    (y[0] +
      2 * y.slice(1, -1).reduce((acc, val) => acc + val, 0) +
      y[y.length - 1]);
  return integral;
}

function titikTengah(f, a, b, n) {
  let h = (b - a) / n;
  let x = a + h / 2;
  let sigma = f(x);
  for (let r = 1; r < n; r++) {
    x += h;
    sigma += f(x);
  }
  let I = sigma * h;
  return I;
}

function metodePiasKaidaSegiempat(f, a, b, n) {
  let h = (b - a) / n;
  let total = 0;
  for (let i = 1; i <= n; i++) {
    let x_i = a + h * (i - 1);
    total += f(x_i);
  }
  let integral = h * total;
  return integral;
}
