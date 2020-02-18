count=0 && until $(curl --output /dev/null --silent --head --fail http://localhost:8080);
  do printf '.' && sleep 3 && count=$((count+1)) && if [ $count -gt 5 ]; then break;
  fi; done
