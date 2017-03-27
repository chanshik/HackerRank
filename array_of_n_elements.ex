defmodule ArrayOfNElements do
  def solve(n) do
    if n == 0 do
      []
    else
      solve(n - 1) ++ [n]
    end
  end

  def main() do
    {n, _} = Integer.parse(IO.gets(""))

    result = Enum.join(Enum.map(solve(n), &(Integer.to_string(&1))), ", ")
    IO.puts("[#{result}]")
  end
end

ArrayOfNElements.main()
