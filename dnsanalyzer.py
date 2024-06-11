import sys
import ipaddress as ipaddr
import openai

openai.api_key = 'your-api-key-here'

def analyze_with_chatgpt(output_text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Analyze the following DNS scan results and provide insights:\n\n{output_text}",
        max_tokens=150
    )
    return response.choices[0].text.strip()

def process_domain(domain, recordtype, args, outfile, addresses, wildcard=None):
    try:
        if sys.stdout.isatty():
            print(f'{domain}\033[K\r', end='')

        res = lookup(domain, recordtype)
        if args.tld and res:
            nameservers = sorted(res)
            ns0 = str(nameservers[0])[:-1]
            print(f'\033[K\r{domain} - {col.brown}{ns0}{col.end}')
            if outfile:
                print(f'{ns0} - {domain}', file=outfile)

        if args.tld and res:
            print(f'\033[K\r{domain} - {res}')
            return

        for rdata in res:
            address = rdata.address
            if wildcard and address in wildcard:
                return

            print('\033[K\r', end='')
            if args.no_ip:
                print(f'{col.brown}{domain}{col.end}')
                break
            elif args.domain_first:
                print(f'{domain} - {col.brown}{address}{col.end}')
            else:
                print(f'{address} - {col.brown}{domain}{col.end}')

            if outfile:
                if args.domain_first:
                    print(f'{domain} - {address}', file=outfile)
                else:
                    print(f'{address} - {domain}', file=outfile)

            try:
                addresses.add(ipaddr.ip_address(str(address)))
            except ValueError:
                addresses.add(ipaddr.ip_address(str(address)))

    except SystemExit:
        sys.exit(0)
    except Exception:
        out.warn("Processing domain failed")

def main():
    wildcard = get_wildcard(target)
    for wildcard_ip in wildcard:
        try:
            addresses.add(ipaddr.ip_address(str(wildcard_ip)))
        except ValueError:
            addresses.add(ipaddr.ip_address(str(wildcard_ip)))

    out.status(f"Scanning {target} for {recordtype} records")
    add_target(target)

    threads = []
    for i in range(args.threads):
        t = scanner(queue)
        t.daemon = True
        t.start()
        threads.append(t)

    try:
        for t in threads:
            t.join(1024)
    except KeyboardInterrupt:
        out.fatal("Caught KeyboardInterrupt, quitting...")
        if outfile:
            outfile.close()
        sys.exit(1)

    print(" " * 40)
    output_text = ""
    if outfile_ips:
        for address in sorted(addresses):
            print(address, file=outfile_ips)
            output_text += f"{address}\n"

    if outfile:
        outfile.close()
    if outfile_ips:
        outfile_ips.close()

    # Send output to ChatGPT for analysis
    chatgpt_analysis = analyze_with_chatgpt(output_text)
    print(f"\nChatGPT Analysis:\n{chatgpt_analysis}\n")

if __name__ == "__main__":
    main()
