defmodule GCD do
  def solve(a, b) do
    cond do
      a == b -> a
      a > b -> solve(a - b, b)
      a < b -> solve(a, b - a)
    end
  end

  def main() do
    [a, b] = Enum.map(
      String.split(IO.gets(""), " "),
      fn (x) -> elem(Integer.parse(x), 0) end)

    IO.puts(solve(a, b))
  end
end

GCD.main()
