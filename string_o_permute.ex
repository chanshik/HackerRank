defmodule StringPermute do
  def solve(s) do
    String.codepoints(s)
    |> Enum.chunk(2)
    |> Enum.map(&(Enum.at(&1, 1) <> Enum.at(&1, 0)))
    |> Enum.join("")
  end

  def main() do
    t = elem(Integer.parse(IO.gets("")), 0)
    arr = for _ <- 1..t do
      IO.gets("")
    end

    for s <- arr do
      IO.puts(solve(s))
    end
  end
end

StringPermute.main()
