defmodule PascalTriangle do
  def pascal_triangle(row, col) do
    cond do
      row <= 1 -> 1
      col == 0 -> 1
      col == row -> 1
      true ->
        pascal_triangle(row - 1, col - 1) + pascal_triangle(row - 1, col)
    end
  end

  def solve(rows) do
    for row <- 0..rows do
      triangle_row = for col <- 0..row do
        pascal_triangle(row, col)
      end

      IO.puts(Enum.join(triangle_row, " "))
    end
  end

  def main() do
    k = elem(Integer.parse(IO.gets("")), 0)

    solve(k - 1)
  end
end

PascalTriangle.main()
