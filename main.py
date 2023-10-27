from db_engine import conn, cur
from rowgen import gen_fn, gen_ln, gen_pn, gen_ptext

def origin_prompt(command:str):
    match command.split():
        case ["rt", start_number, end_number]:
            start_number = int(start_number)
            end_number = int(end_number)
            for i in range(start_number, end_number+1):
                row_fn = gen_fn()
                row_ln = gen_ln()
                row_pn = gen_pn()
                row_pt = gen_ptext()
                cur.execute("REPLACE INTO t_regulartickets(ticketid, firstname, lastname, phonenumber, preferstext) VALUES (?, ?, ?, ?, ?)",
                (i, row_fn, row_ln, row_pn, row_pt))
                print(f"Adding {i}: {row_fn} {row_ln}")
            conn.commit()
        case ["st", start_number, end_number]:
            start_number = int(start_number)
            end_number = int(end_number)
            for i in range(start_number, end_number+1):
                row_fn = gen_fn()
                row_ln = gen_ln()
                row_pn = gen_pn()
                row_pt = gen_ptext()
                cur.execute("REPLACE INTO t_specialtytickets (ticketid, firstname, lastname, phonenumber, preferstext) VALUES (?, ?, ?, ?, ?)",
                (i, row_fn, row_ln, row_pn, row_pt))
                print(f"Adding {i}: {row_fn} {row_ln}")
            conn.commit()
        case ["rb", start_number, end_number]:
            start_number = int(start_number)
            end_number = int(end_number)
            for i in range(start_number, end_number+1):
                cur.execute("SELECT ticketid FROM t_regulartickets ORDER BY RAND() LIMIT 1")
                result = cur.fetchone()[0]
                cur.execute("REPLACE INTO t_regularbaskets (basketid, winningticket) VALUES (?, ?)",
                (i, result))
                print(f"Inserting {i}: {result}")
            conn.commit()
        case ["sb", start_number, end_number]:
            start_number = int(start_number)
            end_number = int(end_number)
            for i in range(start_number, end_number+1):
                cur.execute("SELECT ticketid FROM t_specialtytickets ORDER BY RAND() LIMIT 1")
                result = cur.fetchone()[0]
                cur.execute("REPLACE INTO t_specialtybaskets (basketid, winningticket) VALUES (?, ?)",
                (i, result))
                print(f"Inserting {i}: {result}")
            conn.commit()
        case ["help"]:
            print("You can use the following commands:")
            print("rt start_number end_number   Fills regular tickets between start and end numbers")
            print("st start_number end_number   Fills specialty tickets between start and end numbers")
            print("rb start_number end_number   Fills regular baskets with random winners between start and end.")
            print("sb start_number end_number   Fills specialty baskets with random winners between start and end.")
            print("quit or exit                 Quits the program.")
        case ["quit" | "exit"]:
            print("Bye")
            quit()
        case _:
            print(f"Unknown command {command!r}. Type help and press enter to get a list of commands.")

def main():
    while True:
        cmd = input("TAM Stress Prompt: ")
        origin_prompt(cmd)


if __name__ == "__main__":
    main()