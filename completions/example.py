_example()
{
    COMPREPLY=()
    COMP_WORDBREAKS=" "
    local cur=${COMP_WORDS[COMP_CWORD]}
    local cmd=(${COMP_WORDS[*]})

    if [ "" != "$cur" ]; then
        unset cmd[COMP_CWORD]
    fi

    local choices=$(sudo ${cmd[*]} options)
    COMPREPLY=($(compgen -W '${choices}' -- ${cur} ))
    return 0
}
complete -F _example example.py 
