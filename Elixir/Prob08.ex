main = fn () ->
  [{x, _}, {y, _}] = IO.gets("")
  |> String.trim
  |> String.split(" ")
  |> Enum.map(&Integer.parse/1)

  for i <- 0..19 do
    for j <- 0..19 do

      dist = :math.sqrt(:math.pow(x-i, 2) + :math.pow(y-j, 2))
      |> Kernel.trunc

      val = cond do
        dist == 0 -> 100
        dist == 1 -> 50
        dist == 2 -> 25
        true -> 10
      end

      IO.write(val)
      IO.write(" ")

    end
    IO.puts("")
  end


end




{n, "\n"} = IO.gets("")
  |> Integer.parse

for _ <- 1..n, do: main.()
