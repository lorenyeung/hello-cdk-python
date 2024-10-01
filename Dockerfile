FROM harness/aws-cdk-plugin:1.0.0-python
RUN npm install -g aws-cdk@latest
RUN cdk --version
ADD requirements.txt .
RUN pip3 install -r requirements.txt
