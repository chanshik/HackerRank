defmodule GradingStudents do
  @doc """
  Grading Students
  https://www.hackerrank.com/challenges/grading
  """
  def solve([]) do
    :ok
  end

  def solve(grades) do
    [grade | tail] = grades

    rounded_grade = cond do
      grade < 38 ->
        grade
      rem(grade, 5) >= 3 ->
        (div(grade, 5) + 1) * 5
      true ->
        grade
    end

    IO.puts(rounded_grade)
    solve(tail)
  end

  def main() do
    {n, _} = IO.gets("") |> Integer.parse()
    grades = for _ <- 1..n do
      {grade, _} = IO.gets("") |> Integer.parse()
      grade
    end

    solve(grades)
  end
end

GradingStudents.main()
