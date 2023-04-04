

if __name__ == '__main__':
    import adn as module_adn
    from adn import poucentage_sequence, occurences_sequence
    # module_adn.main()

    occ = occurences_sequence("abc" , "abcdabc")
    print(occ)
    pct = poucentage_sequence(occ, "abc", "abcdabc")
    print(round(pct, 3))