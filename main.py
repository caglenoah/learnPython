def take_magic_damage(health, resist, amp, spell_power):
   max_damage = amp * spell_power
   actual_damage = max_damage - resist
   new_health = health - actual_damage
   return new_health
