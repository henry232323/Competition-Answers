defmodule Problem do
  def find_divergence(re, im, zr, zi, n) do
      fr = :math.pow(zr, 2) - :math.pow(zi, 2) + re
      fi = 2 * zi * zr + im

      cond do
        n > 50 -> n
        (:math.pow(fr, 2) + :math.pow(fi, 2) > :math.pow(100, 2)) -> n
        true -> find_divergence(re, im, fr, fi, n+1)
      end
  end

  def find_divergence(re, im) do
    find_divergence(re, im, 0, 0, 0)
  end

  def main() do
    [rst, ist] = IO.gets("")
    |> String.trim
    |> String.split(" ")

    {real, _} = Float.parse(rst)
    {imag, _} = Float.parse(ist)

    dn = find_divergence(real, imag)
    color = cond do
      dn <= 10 -> "i RED"
      dn <= 20 -> "i ORANGE"
      dn <= 30 -> "i YELLOW"
      dn <= 40 -> "i GREEN"
      dn <= 50 -> "i BLUE"
      true -> "i BLACK"
    end

    sign = if (imag >= 0) do
      "+"
    else
      ""
    end

    IO.puts(rst <> sign <> ist <> color)

  end
end


{n, "\n"} = IO.gets("")
  |> Integer.parse

for _ <- 1..n, do: Problem.main()
