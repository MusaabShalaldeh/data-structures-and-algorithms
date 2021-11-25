from data_strtucture.hash_tables.hash_tables import HashTable

def find_most_used(book: str):
    words = book.split(" ")
    hashtable = HashTable()
    most_used_word = ""

    for i in words:
        val_in_table = hashtable.get(i)
        counter = 0
        if val_in_table:
            val = val_in_table + 1
            hashtable.add(i,val)
            if(val > counter):
                most_used_word = i
        else:
            hashtable.add(i,1)

    return most_used_word

