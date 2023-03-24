if __name__ == '__main__':
    with open('gcrio.txt', 'r') as fr:
        with open('new_gcrio.txt', 'w') as fw:
            lines = fr.readlines()
            write_lines = []
            for line in lines:
                write_lines.append('- name: ' + line)
                newName = 'm.daocloud.io/' + \
                    line.split(":")[0].split('@')[0] + '\n'
                write_lines.append('  newName: ' + newName)
                newTag = line.split(':')[1]
                write_lines.append('  newTag: "' + newTag[0:-1] + '"\n')
            fw.writelines(write_lines)
