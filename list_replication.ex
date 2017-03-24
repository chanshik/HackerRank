defmodule ListReplication do
  @moduledoc false
  def replicate(_, []) do
    :ok
  end

  def replicate(n, arr) do
    [head | tail] = arr

    for _ <- 1..n do
      IO.puts(head)
    end
    replicate(n, tail)
  end

  def input_loop(elements \\ []) do
    case IO.gets("") do
      :eof -> elements
      "\n" -> elements
      data ->
        {element, _} = Integer.parse(data)

        input_loop(elements ++ [element])
    end
  end

  def main() do
    {n, _} = Integer.parse(IO.gets(""))

    replicate(n, input_loop([]))
  end
end

ListReplication.main()
