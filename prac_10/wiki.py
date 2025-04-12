import wikipedia

def main():
    print("Wikipedia page search")
    while True:
        search_term = input("Enter page title: ").strip()
        if not search_term:
            print("Thank you.")
            break
        try:
            # 검색어로 Wikipedia 페이지 얻기
            page = wikipedia.page(search_term, auto_suggest=False)
            print(page.title)
            print(wikipedia.summary(search_term, auto_suggest=False))
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{search_term}" does not match any pages. Try another id!')

if __name__ == "__main__":
    main()
