class DimentionError(Exception):
    pass


def input_matrix():
    """
    read matrix(str) n*n from input

    Parametes
    ----------------

    Returns
    ----------------
    list -> 2D

    """

    try:
        n = int(input("Enter the shape of matrix (n):"))

        matrix = []
        print("Enter each row of matrix:")
        for _ in range(n):
            row = input().strip()
            if not row.isalpha():
                raise ValueError("The input must be character!")
            if len(row) != n:
                raise DimentionError(
                    f"The expected length of the input array is {n} but has been received {len(row)}.")
            matrix.append(row.lower())
        response = matrix
    except DimentionError as e:
        response = e
    except ValueError as e:
        response = e
    except Exception as e:
        response = e
    finally:
        return response
