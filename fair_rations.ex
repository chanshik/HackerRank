defmodule FairRations do
  require Integer
  @doc """
  Fair Rations
  https://www.hackerrank.com/challenges/fair-rations
  """
  def solve([], _, loaves) do
    loaves
  end

  def solve(persons, add_more, loaves) do
    [head | tail] = persons
    head = head + add_more

    if Integer.is_odd(head) do
      solve(tail, 1, loaves + 2)
    else
      solve(tail, 0, loaves)
    end
  end

  def main() do
    _ = IO.gets("")
    persons = IO.gets("")
    |> String.trim()
    |> String.split(" ")
    |> Enum.map(fn (x) -> elem(Integer.parse(x), 0) end)

    if Integer.is_odd(Enum.sum(persons)) do
      IO.puts("NO")
    else
      IO.puts(solve(persons, 0, 0))
    end
  end
end

FairRations.main()
