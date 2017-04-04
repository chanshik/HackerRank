defmodule Fibonacci do
  def solve(n) do
    cond do
      n == 0 -> 0
      n == 1 -> 0
      n == 2 -> 1
      n > 2 -> solve(n - 1) + solve(n - 2)
    end
  end

  def main() do
    n = elem(Integer.parse(IO.gets("")), 0)

    IO.puts(solve(n))
  end
end

Fibonacci.main()
