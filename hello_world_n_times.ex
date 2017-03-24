defmodule HelloWorldNTimes do
  @moduledoc false
  def solve(n) do
    for _ <- 1..n do
      IO.puts("Hello World")
    end
  end

  def main(args \\ []) do
    {n, _} = Integer.parse(IO.gets(""))

    solve(n)
  end
end

HelloWorldNTimes.main()
