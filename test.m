extractCommand = sprintf('test.bat %s', ...
    'E:\gandalf_20240112_g0\gandalf_20240112_g0_imec3\gandalf_20240112_g0_imec3_ks_cat');
fprintf('  Bash command: %s\n', extractCommand)
system(extractCommand);
disp(5+5);
disp('testing for blocking in system')