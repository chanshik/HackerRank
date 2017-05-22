defmodule PowerSum do
  @doc """
  https://www.hackerrank.com/challenges/the-power-sum
  """
  def solve(x, _, sums) when x == 0 do
    IO.puts("Matched: #{sums}")
    IO.inspect(sums)
    1
  end

  def solve(x, n, sums) do
    limit_left = trunc(:math.pow(x, 1.0 / n))

    results = for i <- limit_left..1 do
      cond do
        i in sums -> 0
        i > Enum.at(sums, -1) -> 0
        x - :math.pow(i, n) >= 0 ->
          solve(x - :math.pow(i, n), n, sums ++ [i])
        true -> 0
      end
    end

    Enum.sum(results)
  end

  def main() do
    {x, _} = IO.gets("") |> Integer.parse()
    {n, _} = IO.gets("") |> Integer.parse()

    IO.puts(solve(x, n, []))
  end
end

PowerSum.main()
