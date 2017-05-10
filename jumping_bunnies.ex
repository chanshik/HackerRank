defmodule GCD do
  @doc """
  Jumping Bunnies

  https://www.hackerrank.com/challenges/jumping-bunnies
  """

  def solve(a, b) do
    cond do
      a == b -> a
      a > b ->
        remain = rem(a, b)
        if remain == 0 do
          b
        else
          solve(remain, b)
        end
      a < b ->
        remain = rem(b, a)
        if remain == 0 do
          a
        else
          solve(a, remain)
        end
    end
  end
end

defmodule JumpingBunnies do
  def solve(distances) do
    [acc | distances] = [hd(distances) | tl(distances)]

    Enum.reduce(distances, acc,
      fn (d, acc) -> div(d, GCD.solve(d, acc)) * acc end)
  end

  def main() do
    _ = elem(Integer.parse(IO.gets("")), 0)
    distances = IO.gets("")
    |> String.trim()
    |> String.split(" ")
    |> Enum.map(&(elem(Integer.parse(&1), 0)))
    |> Enum.sort()

    IO.puts(solve(distances))
  end
end

JumpingBunnies.main()
